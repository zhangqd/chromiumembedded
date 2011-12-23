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

#include "libcef_dll/ctocpp/domdocument_ctocpp.h"
#include "libcef_dll/ctocpp/domnode_ctocpp.h"


// VIRTUAL METHODS - Body may be edited by hand.

CefDOMDocument::Type CefDOMDocumentCToCpp::GetType()
{
  if (CEF_MEMBER_MISSING(struct_, get_type))
    return DOM_DOCUMENT_TYPE_UNKNOWN;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_dom_document_type_t _retval = struct_->get_type(struct_);

  // Return type: simple
  return _retval;
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetDocument()
{
  if (CEF_MEMBER_MISSING(struct_, get_document))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_document(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetBody()
{
  if (CEF_MEMBER_MISSING(struct_, get_body))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_body(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetHead()
{
  if (CEF_MEMBER_MISSING(struct_, get_head))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_head(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

CefString CefDOMDocumentCToCpp::GetTitle()
{
  if (CEF_MEMBER_MISSING(struct_, get_title))
    return CefString();

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_string_userfree_t _retval = struct_->get_title(struct_);

  // Return type: string
  CefString _retvalStr;
  _retvalStr.AttachToUserFree(_retval);
  return _retvalStr;
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetElementById(const CefString& id)
{
  if (CEF_MEMBER_MISSING(struct_, get_element_by_id))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Verify param: id; type: string_byref_const
  DCHECK(!id.empty());
  if (id.empty())
    return NULL;

  // Execute
  cef_domnode_t* _retval = struct_->get_element_by_id(struct_,
      id.GetStruct());

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetFocusedNode()
{
  if (CEF_MEMBER_MISSING(struct_, get_focused_node))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_focused_node(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

bool CefDOMDocumentCToCpp::HasSelection()
{
  if (CEF_MEMBER_MISSING(struct_, has_selection))
    return false;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  int _retval = struct_->has_selection(struct_);

  // Return type: bool
  return _retval?true:false;
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetSelectionStartNode()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_start_node))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_selection_start_node(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

int CefDOMDocumentCToCpp::GetSelectionStartOffset()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_start_offset))
    return 0;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  int _retval = struct_->get_selection_start_offset(struct_);

  // Return type: simple
  return _retval;
}

CefRefPtr<CefDOMNode> CefDOMDocumentCToCpp::GetSelectionEndNode()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_end_node))
    return NULL;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_domnode_t* _retval = struct_->get_selection_end_node(struct_);

  // Return type: refptr_same
  return CefDOMNodeCToCpp::Wrap(_retval);
}

int CefDOMDocumentCToCpp::GetSelectionEndOffset()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_end_offset))
    return 0;

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  int _retval = struct_->get_selection_end_offset(struct_);

  // Return type: simple
  return _retval;
}

CefString CefDOMDocumentCToCpp::GetSelectionAsMarkup()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_as_markup))
    return CefString();

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_string_userfree_t _retval = struct_->get_selection_as_markup(struct_);

  // Return type: string
  CefString _retvalStr;
  _retvalStr.AttachToUserFree(_retval);
  return _retvalStr;
}

CefString CefDOMDocumentCToCpp::GetSelectionAsText()
{
  if (CEF_MEMBER_MISSING(struct_, get_selection_as_text))
    return CefString();

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_string_userfree_t _retval = struct_->get_selection_as_text(struct_);

  // Return type: string
  CefString _retvalStr;
  _retvalStr.AttachToUserFree(_retval);
  return _retvalStr;
}

CefString CefDOMDocumentCToCpp::GetBaseURL()
{
  if (CEF_MEMBER_MISSING(struct_, get_base_url))
    return CefString();

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Execute
  cef_string_userfree_t _retval = struct_->get_base_url(struct_);

  // Return type: string
  CefString _retvalStr;
  _retvalStr.AttachToUserFree(_retval);
  return _retvalStr;
}

CefString CefDOMDocumentCToCpp::GetCompleteURL(const CefString& partialURL)
{
  if (CEF_MEMBER_MISSING(struct_, get_complete_url))
    return CefString();

  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  // Verify param: partialURL; type: string_byref_const
  DCHECK(!partialURL.empty());
  if (partialURL.empty())
    return CefString();

  // Execute
  cef_string_userfree_t _retval = struct_->get_complete_url(struct_,
      partialURL.GetStruct());

  // Return type: string
  CefString _retvalStr;
  _retvalStr.AttachToUserFree(_retval);
  return _retvalStr;
}


#ifndef NDEBUG
template<> long CefCToCpp<CefDOMDocumentCToCpp, CefDOMDocument,
    cef_domdocument_t>::DebugObjCt = 0;
#endif

