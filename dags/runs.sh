# https://unix.stackexchange.com/questions/285687/a-quicker-way-to-change-owner-group-recursively
sudo apt-get update
#sudo pip install bs4
#sudo pip install selenium
sudo pip install aiohttp
sudo pip install sqlalchemy
sudo pip install --pre --upgrade bs4
sudo pip install --pre --upgrade selenium
sudo pip install --pre --upgrade aiohttp
sudo pip install --pre --upgrade glob2
sudo pip install --pre --upgrade urllib3
#sudo python3 -m pip install --pre --upgrade mock #>=2.0
#sudo python3 -m pip install --pre --upgrade pyqt5 #>=5.12
#sudo python3 -m pip install --pre --upgrade typed-ast #>=1.3.0
#sudo python -m pip install dask[dataframe]
#sudo python3 -m pip install --pre --upgrade tables #==3.5.1
#sudo python3 -m pip install --pre --upgrade astroid #==2.2.5
#sudo python3 -m pip install --pre --upgrade "dask[complete]"
#sudo python3 -m pip install --pre --upgrade dask[complete]

#sudo python3 -m pip install --pre --upgrade Toolz
#sudo python3 -m pip install --pre --upgrade Tornado
cd ..
sudo chown -R osboxes:osboxes * .[^.]*
cd /dags
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
sudo chmod +x /usr/bin/geckodriver
rm geckodriver-v0.23.0-linux64.tar.gz

#python3 -m pip install --pre --upgrade PACKAGE==VERSION.VERSION.VERSION
