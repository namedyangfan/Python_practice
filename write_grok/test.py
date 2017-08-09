import os
from write_grok import Write_grok
import glob
grok_directory = r"D:\ARB\HGS_Simulations\Sub_Assiniboine\steve_Jun\26-31-SARB_monthly_47764Nodes"
grok_name = "ARB_ASSN.grok"
target_times=[32875200.0, 35424000.0, 37972800.0, 40608000.0, 43243200.0, 45878400.0, 48513600.0, 51192000.0, 53827200.0, 56462400.0, 59097600.0, 61732800.0, 64411200.0, 66960000.0, 69508800.0, 72144000.0, 74779200.0, 77414400.0, 80049600.0, 82728000.0, 85363200.0, 87998400.0, 90633600.0, 93268800.0]

gr = Write_grok(grok_name=grok_name, grok_directory=grok_directory)
gr.add_gw_wells(inc_file_name="ARB_subassin_obs.inc",overwrite=True)
gr.add_target_output_times(out_times=[0.932688500E+008], target_times=target_times, overwrite=True)

grok_directory = r"D:\ARB\HGS_Simulations\Qu_Appelle\Steve_Jun_51250nodes\26-32-QRB_daily_51250Nodes"
grok_name = "ARB_QUAP.grok"
target_times=[32875200.0, 35424000.0, 37972800.0, 40608000.0, 43243200.0, 45878400.0, 48513600.0, 51192000.0, 53827200.0, 56462400.0, 59097600.0, 61732800.0, 64411200.0, 66960000.0, 69508800.0, 72144000.0, 74779200.0, 77414400.0, 80049600.0, 82728000.0, 85363200.0, 87998400.0, 90633600.0, 93268800.0]

gr = Write_grok(grok_name=grok_name, grok_directory=grok_directory)
gr.add_gw_wells(inc_file_name="obs_wells.inc",overwrite=True)
gr.add_target_output_times(out_times=[0.932688500E+008], target_times=target_times, overwrite=True)

