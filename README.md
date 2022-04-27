# SteamFamilySharingManager
Useful tool to manage the priority of multiple Steam Family Shared libraries

Before Starting the application do the following things, otherwise the software could incoure in some problems and may not save the changes you have made to the list:
1. Make sure Steam application is closed (check the Task Manager).
2. Open SteamSettings.py file and change ``STEAM_PATH`` with your steam installation folder if it is not correct.
3. Go to  **[Steam API key site](https://steamcommunity.com/dev/apikey)**, login and generate a Steam API key (you can use as a domain name "127.0.0.1", it doesn't matter) and modify ``KEY`` in the SteamSettings.py (this is made to not violate Steam Terms of Service users are not allowed to share theirs keys, so everyone needs to use their own key).

After you are done with step ****1****, ****2****, ****3**** you can run the SteamFamilySharingManager.py file, at this point follow the subsequent steps:
1. After that you can insert the two indicies of the users you want to swap shown in the list.
2. Repeat the swapping process as many times you want, anserwing to the question "Continue(y/n)?" "y" to continue the process or "n" end it.
3. Enjoy your shared steam libraries in the order you want (maybe) without any problem.
