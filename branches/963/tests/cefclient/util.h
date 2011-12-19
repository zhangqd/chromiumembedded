// Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.

#ifndef _CEFCLIENT_UTIL_H
#define _CEFCLIENT_UTIL_H

#include "include/cef.h"

#if defined(OS_WIN)

#include <windows.h>

#ifndef NDEBUG
#define ASSERT(condition) if(!(condition)) { DebugBreak(); }
#else
#define ASSERT(condition) ((void)0)
#endif

#else // !OS_WIN

#include <assert.h>

#ifndef NDEBUG
#define ASSERT(condition) if(!(condition)) { assert(false); }
#else
#define ASSERT(condition) ((void)0)
#endif

#endif // !OS_WIN

#define REQUIRE_UI_THREAD()   ASSERT(CefCurrentlyOn(TID_UI));
#define REQUIRE_IO_THREAD()   ASSERT(CefCurrentlyOn(TID_IO));
#define REQUIRE_FILE_THREAD() ASSERT(CefCurrentlyOn(TID_FILE));

#endif // _CEFCLIENT_UTIL_H
