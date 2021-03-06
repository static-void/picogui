/* $Id: if_pntr_preprocess.c 4551 2003-09-03 18:22:27Z Dentoid $
 *
 * if_pntr_preprocess.c - Various processing on mouse pointer events before dispatch
 *
 * PicoGUI small and efficient client/server GUI
 * Copyright (C) 2000-2003 Micah Dowty <micahjd@users.sourceforge.net>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA 
 * 
 * Contributors:
 * 
 * 
 * 
 */

#include <pgserver/common.h>
#include <pgserver/input.h>

void infilter_pntr_preprocess_handler(struct infilter *self, u32 trigger, union trigparam *param) {

  /* Convert the event to logical coordinates if necessary
   */
  if (!param->mouse.is_logical) {
    /* Scroll wheel events always logical */
    if (trigger != PG_TRIGGER_SCROLLWHEEL)
      VID(coord_logicalize)(&param->mouse.x, &param->mouse.y);
    param->mouse.is_logical = 1;
  }
}

struct infilter infilter_pntr_preprocess = {
  /*accept_trigs:  */PG_TRIGGER_UP | PG_TRIGGER_DOWN | PG_TRIGGER_MOVE | PG_TRIGGER_SCROLLWHEEL,
  /*absorb_trigs:  */0,
       /*handler:  */&infilter_pntr_preprocess_handler
};

/* The End */






