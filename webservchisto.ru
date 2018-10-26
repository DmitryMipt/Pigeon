server{
        listen 80;
        server_name webservchisto.ru www.webservchisto.ru;
location ~ \.(gif|jpg|png)$ {
                root /home/dmitry/Pigeon/public/pictures;
        }
        location / {
                root /home/dmitry/Pigeon/public;

                index index.html;
        }
        location /api/ {
        proxy_pass         http://127.0.0.1:8000;
        proxy_redirect     off;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Host $server_name;
        }
}
