#%%
import os

def quit_all_chrome():
    os.system("pkill -f 'Google Chrome'")
    print("All Chrome browsers have been closed.")

# Call the function to quit all Chrome browsers
quit_all_chrome()

