import os
from smm_wrapper import SMM


# Examples using the api directly
smm = SMM()
last_rev_content = smm.dv.last_rev_content(2161298)
df = smm.dv.specific_rev_content_by_rev_id(503680497)

page = smm.api.edit_persistence(page_id=2161298)
editor = smm.api.edit_persistence(editor_id=28481209)
page_editor = smm.api.edit_persistence(page_id=2161298, editor_id=286968)

edit_persistence_by_page_id_df = smm.dv.edit_persistence(page_id=2161298)
edit_persistence_by_editor_id_df = smm.dv.edit_persistence(editor_id=28481209)
edit_persistence_by_page_id_and_editor_id_df = smm.dv.edit_persistence(
    page_id=2161298, editor_id=286968)

import ipdb; ipdb.set_trace()  # breakpoint 67efd4b1 //
