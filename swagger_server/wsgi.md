1. add files to apache conf
    sudo vim /etc/apache2/sites-enabled/api.conf
    
    conf:
    ```buildoutcfg
        Listen 8080
        
        <VirtualHost *:8080>
             # Add machine's IP address (use ifconfig command)
             ServerName goodclass.cf
             # Give an alias to to start your website url with
             WSGIScriptAlias / /home/thetawang/Gooditem_class/swagger_server/flask_app.wsgi
             <Directory /home/thetawang/Gooditem_class/swagger_server/>
                        # set permissions as per apache2.conf file
                    Options FollowSymLinks
                    AllowOverride None
                    Require all granted
             </Directory>
             ErrorLog ${APACHE_LOG_DIR}/error-api.log
             LogLevel warn
             CustomLog ${APACHE_LOG_DIR}/access-api.log combined
             SSLCertificateFile /etc/letsencrypt/live/goodclass.cf/fullchain.pem
             SSLCertificateKeyFile /etc/letsencrypt/live/goodclass.cf/privkey.pem
             Include /etc/letsencrypt/options-ssl-apache.conf
        </VirtualHost>

    ```
2. confirm conf be loaded

    `sudo apachectl -t -D DUMP_VHOSTS`

3. reload conf

    `sudo /etc/init.d/apache2 reload`

4. log
    ```
    sudo vim /var/log/apache2/error-api.log
    sudo vim /var/log/apache2/access-api.log
    ```