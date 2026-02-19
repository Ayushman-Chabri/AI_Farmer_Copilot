It provides support in three phases:
Before sowing (planning)
During crop growth (monitoring + disease help)
After harvest (selling + yield evaluation)
This file ensures the system activates the correct module for each phase.

-----------------
0.4 Give options for Modes
Pre-cropping
Cropping
Post-cropping
This file implements exactly that routing step.

| Parameter | Type   | Meaning                                                           |
| --------- | ------ | ----------------------------------------------------------------- |
| mode      | string | Farmer-selected stage (`precropping`, `cropping`, `postcropping`) |