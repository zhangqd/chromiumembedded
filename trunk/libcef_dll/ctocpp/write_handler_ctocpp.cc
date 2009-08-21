// Copyright (c) 2009 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.
//
// ---------------------------------------------------------------------------
//
// A portion of this file was generated by the CEF translator tool.  When
// making changes by hand only do so within the body of existing static and
// virtual method implementations. See the translator.README.txt file in the
// tools directory for more information.
//

#include "../precompiled_libcef.h"
#include "ctocpp/write_handler_ctocpp.h"


// VIRTUAL METHODS - Body may be edited by hand.

size_t CefWriteHandlerCToCpp::Write(const void* ptr, size_t size, size_t n)
{
  if(CEF_MEMBER_MISSING(struct_, write))
    return 0;

  return struct_->write(struct_, ptr, size, n);
}

int CefWriteHandlerCToCpp::Seek(long offset, int whence)
{
  if(CEF_MEMBER_MISSING(struct_, seek))
    return 0;

  return struct_->seek(struct_, offset, whence);
}

long CefWriteHandlerCToCpp::Tell()
{
  if(CEF_MEMBER_MISSING(struct_, tell))
    return 0;

  return struct_->tell(struct_);
}

int CefWriteHandlerCToCpp::Flush()
{
  if(CEF_MEMBER_MISSING(struct_, flush))
    return 0;

  return struct_->flush(struct_);
}


#ifdef _DEBUG
long CefCToCpp<CefWriteHandlerCToCpp, CefWriteHandler,
    cef_write_handler_t>::DebugObjCt = 0;
#endif

