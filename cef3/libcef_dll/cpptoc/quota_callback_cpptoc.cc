// Copyright (c) 2012 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.
//
// ---------------------------------------------------------------------------
//
// This file was generated by the CEF translator tool. If making changes by
// hand only do so within the body of existing method and function
// implementations. See the translator.README.txt file in the tools directory
// for more information.
//

#include "libcef_dll/cpptoc/quota_callback_cpptoc.h"


// MEMBER FUNCTIONS - Body may be edited by hand.

void CEF_CALLBACK quota_callback_cont(struct _cef_quota_callback_t* self,
    int allow) {
  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  DCHECK(self);
  if (!self)
    return;

  // Execute
  CefQuotaCallbackCppToC::Get(self)->Continue(
      allow?true:false);
}

void CEF_CALLBACK quota_callback_cancel(struct _cef_quota_callback_t* self) {
  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  DCHECK(self);
  if (!self)
    return;

  // Execute
  CefQuotaCallbackCppToC::Get(self)->Cancel();
}


// CONSTRUCTOR - Do not edit by hand.

CefQuotaCallbackCppToC::CefQuotaCallbackCppToC(CefQuotaCallback* cls)
    : CefCppToC<CefQuotaCallbackCppToC, CefQuotaCallback, cef_quota_callback_t>(
        cls) {
  struct_.struct_.cont = quota_callback_cont;
  struct_.struct_.cancel = quota_callback_cancel;
}

#ifndef NDEBUG
template<> long CefCppToC<CefQuotaCallbackCppToC, CefQuotaCallback,
    cef_quota_callback_t>::DebugObjCt = 0;
#endif

