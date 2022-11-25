if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/YourUsername/ATG-Shortener-V2.git /ATG-Shortener-V2
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /ATG-Shortener-V2
fi
cd /ATG-Shortener-V2
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m main
