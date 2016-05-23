mysql -u root -e "CREATE database sm_web CHARACTER SET = utf8;"
mysql -u root -e "CREATE user 'sm_web_user'@'localhost';"
mysql -u root -e "SET PASSWORD FOR 'sm_web_user'@'localhost' = PASSWORD('p');" -p
mysql -u root -e "GRANT all ON sm_web.* TO 'sm_web_user';"
