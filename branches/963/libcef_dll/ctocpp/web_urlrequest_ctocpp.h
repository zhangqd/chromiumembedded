// Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
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

#ifndef _WEBURLREQUEST_CTOCPP_H
#define _WEBURLREQUEST_CTOCPP_H

#ifndef USING_CEF_SHARED
#pragma message("Warning: "__FILE__" may be accessed wrapper-side only")
#else // USING_CEF_SHARED

#include "include/cef.h"
#include "include/cef_capi.h"
#include "libcef_dll/ctocpp/ctocpp.h"

// Wrap a C structure with a C++ class.
// This class may be instantiated and accessed wrapper-side only.
class CefWebURLRequestCToCpp
    : public CefCToCpp<CefWebURLRequestCToCpp, CefWebURLRequest,
        cef_web_urlrequest_t>
{
public:
  CefWebURLRequestCToCpp(cef_web_urlrequest_t* str)
      : CefCToCpp<CefWebURLRequestCToCpp, CefWebURLRequest,
          cef_web_urlrequest_t>(str) {}
  virtual ~CefWebURLRequestCToCpp() {}

  // CefWebURLRequest methods
  virtual void Cancel() OVERRIDE;
  virtual RequestState GetState() OVERRIDE;
};

#endif // USING_CEF_SHARED
#endif // _WEBURLREQUEST_CTOCPP_H

