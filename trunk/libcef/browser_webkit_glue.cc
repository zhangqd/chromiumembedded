// Copyright (c) 2008-2009 The Chromium Embedded Framework Authors.
// Portions copyright (c) 2006-2008 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/compiler_specific.h"

#include "third_party/WebKit/Source/WebCore/config.h"
MSVC_PUSH_WARNING_LEVEL(0);
#include "DocumentLoader.h"
#include "MemoryCache.h"
#include "TextEncoding.h"
#include "third_party/WebKit/WebKit/chromium/src/WebFrameImpl.h"
MSVC_POP_WARNING();
#undef LOG
#include "base/string_util.h"
#include "net/base/mime_util.h"
#include "webkit/plugins/npapi/plugin_list.h"

#include "browser_webkit_glue.h"

#undef LOG
#include "cef_context.h"

#include "base/logging.h"
#include "base/path_service.h"
#include "base/scoped_ptr.h"
#include "base/string16.h"
#include "net/base/mime_util.h"
#include "third_party/WebKit/WebKit/chromium/public/WebFrame.h"
#include "third_party/WebKit/WebKit/chromium/public/WebString.h"
#include "webkit/glue/webkit_glue.h"
#include "webkit/glue/plugins/plugin_list.h"

// Generated by GRIT
#include "grit/webkit_resources.h"

using WebKit::WebFrameImpl;

namespace webkit_glue {

bool IsMediaPlayerAvailable() {
  return true;
}

void PrecacheUrl(const char16* url, int url_length) {}

void AppendToLog(const char* file, int line, const char* msg) {
  logging::LogMessage(file, line).stream() << msg;
}

bool GetApplicationDirectory(FilePath* path) {
  return PathService::Get(base::DIR_EXE, path);
}

bool GetExeDirectory(FilePath* path) {
  return PathService::Get(base::DIR_EXE, path);
}

bool IsPluginRunningInRendererProcess() {
  return true;
}

bool GetPluginFinderURL(std::string* plugin_finder_url) {
  return false;
}

void GetPlugins(bool refresh,
                std::vector<webkit::npapi::WebPluginInfo>* plugins) {
  webkit::npapi::PluginList::Singleton()->GetPlugins(refresh, plugins);
}

bool IsDefaultPluginEnabled() {
  return false;
}

bool IsProtocolSupportedForMedia(const GURL& url) {
  if (url.SchemeIsFile() || url.SchemeIs("http") || url.SchemeIs("https"))
    return true;
  return false;
}

std::string GetWebKitLocale() {
  const CefSettings& settings = _Context->settings();
  if (settings.locale.length > 0)
    return CefString(&settings.locale);
  return "en-US";
}

void InitializeTextEncoding() {
  WebCore::UTF8Encoding();
}

v8::Handle<v8::Context> GetV8Context(WebKit::WebFrame* frame)
{
  WebFrameImpl* webFrameImpl = static_cast<WebFrameImpl*>(frame);
  WebCore::Frame* core_frame = webFrameImpl->frame();
  return WebCore::V8Proxy::context(core_frame);
}

FrameLoadType GetFrameLoadType(WebKit::WebFrame* frame)
{
  WebFrameImpl* webFrameImpl = static_cast<WebFrameImpl*>(frame);
  WebCore::FrameLoader* loader = webFrameImpl->frame()->loader();
  switch(loader->loadType()) {
    case WebCore::FrameLoadTypeStandard:
      return FLT_STANDARD;
    case WebCore::FrameLoadTypeForward:
    case WebCore::FrameLoadTypeBack:
    case WebCore::FrameLoadTypeBackWMLDeckNotAccessible:
    case WebCore::FrameLoadTypeIndexedBackForward:
      return FLT_HISTORY;
    case WebCore::FrameLoadTypeRedirectWithLockedBackForwardList:
      return FLT_REDIRECT;
    case WebCore::FrameLoadTypeReload:
    case WebCore::FrameLoadTypeReloadFromOrigin:
    case WebCore::FrameLoadTypeSame:
    case WebCore::FrameLoadTypeReplace:
      return FLT_RELOAD;
  }

  return FLT_UNKNOWN;
}

bool FrameHasSubsituteData(WebKit::WebFrame* frame)
{
  WebFrameImpl* webFrameImpl = static_cast<WebFrameImpl*>(frame);
  WebCore::DocumentLoader* docLoader =
      webFrameImpl->frame()->loader()->documentLoader();
  return docLoader->substituteData().isValid();
}

void CloseIdleConnections() {
  // Used in benchmarking,  Ignored for CEF.
}

void SetCacheMode(bool enabled) {
  // Used in benchmarking,  Ignored for CEF.
}

void ClearCache()
{
  // Clear the cache by disabling it and then re-enabling it.
  WebCore::cache()->setDisabled(true);
  WebCore::cache()->setDisabled(false);
}

std::string GetProductVersion() {
  const CefSettings& settings = _Context->settings();
  if (settings.product_version.length > 0) {
    return CefString(&settings.product_version);
  }
  return "Chrome/7.0.517.0";
}

bool IsSingleProcess() {
  return true;
}

#if defined(OS_LINUX)
int MatchFontWithFallback(const std::string& face, bool bold,
                          bool italic, int charset) {
  return -1;
}

bool GetFontTable(int fd, uint32_t table, uint8_t* output,
                  size_t* output_length) {
  return false;
}
#endif

void EnableSpdy(bool enable) {
  // Used in benchmarking,  Ignored for CEF.
}

// Adapted from Chromium's BufferedResourceHandler::ShouldDownload
bool ShouldDownload(const std::string& content_disposition,
                    const std::string& mime_type)
{
  std::string type = StringToLowerASCII(mime_type);
  std::string disposition = StringToLowerASCII(content_disposition);

  // First, examine content-disposition.
  if (!disposition.empty()) {
    bool should_download = true;

    // Some broken sites just send ...
    //    Content-Disposition: ; filename="file"
    // ... screen those out here.
    if (disposition[0] == ';')
      should_download = false;

    if (disposition.compare(0, 6, "inline") == 0)
      should_download = false;

    // Some broken sites just send ...
    //    Content-Disposition: filename="file"
    // ... without a disposition token... Screen those out.
    if (disposition.compare(0, 8, "filename") == 0)
      should_download = false;

    // Also in use is Content-Disposition: name="file"
    if (disposition.compare(0, 4, "name") == 0)
      should_download = false;

    // We have a content-disposition of "attachment" or unknown.
    // RFC 2183, section 2.8 says that an unknown disposition
    // value should be treated as "attachment".
    if (should_download)
      return true;
  }

  // Mirrors WebViewImpl::CanShowMIMEType()
  if (type.empty() || net::IsSupportedMimeType(type))
    return false;

  //// Finally, check the plugin list.
  webkit::npapi::WebPluginInfo info;
  bool allow_wildcard = false;
  return !webkit::npapi::PluginList::Singleton()->GetPluginInfo(
    GURL(), type, allow_wildcard, &info, NULL) || !info.enabled;
}

}  // namespace webkit_glue
