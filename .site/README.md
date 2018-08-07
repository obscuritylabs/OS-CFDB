# OS-CFDB-SITE

## Development Stack 
The development stack is in-line with the production stack and is easy to configure and build.

Start by obtaining the repo via git:
```
git clone https://github.com/obscuritylabs/OS-CFDB.git
```
Make sure you have docker + docker-compose installed and run the following:
```
cd OS-CFDB/.site && chmod +x build.sh && ./build.sh
```
Open a browser and navigate to:
```
open https://127.0.0.1/
```

## Production Stack
The production stack deployment is wholly automated via ansible, docker, docker-compose. The cfdb stack currently only supports single-instance configurations (Mostly because it's not a demanding resource, and caching is used heavily). 

### OS-CFDB Stack Components
Currently, the stack makes use of the latest version's of:

1) Docker - Container & networking for all components
2) Docker Compose - Orchristrate network links & resources 
3) Ansible - Production AWS install
4) Nginx - Reverse proxy -> uwsgi protocol (UNIX Sockets)
5) Python 3 Flask RESTful API - Backend
6) Python 3 Flask UI - Frontend
7) MongoDB - Finding repository document storage
8) Redis - API/View route caching & rate-limiting 
7) uWSGI - Host Flask logic
8) Cloudflare - Protect the host, web components & true public IP


### Deploy to AWS
Deploying to AWS requires a few steps to configure your environment correctly. A list of required packages can be easily found in the `.travis.yml` File. We have tested the deployment for MacOS and Ubuntu and is daily executed via a simple CI pipeline. This builds from master on any push and a Travis CI Cron job, it includes a full docker environment + AWS configuration with a new configuration!

Setup ENV vars for the ansible Playbook (**these are required**)
```
export cloudflare_account_email=YOUREMAILHERE@email.com
export cloudflare_api_token=YOURTOKENHERE
export aws_access_key=YOURACCESSKEY
export aws_secret_key=YOURSECRETKEYHERE
```

**HINT:** Where can I find my secret data?

- Cloudflare API key - https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-
- AWS API keys - https://docs.aws.amazon.com/general/latest/gr/managing-was-access-keys.html
