## How to run
Put `.env` and `.env.dev` file in the root directory

## Production
Build: `docker build -t auth .`<br>
Run: `docker run -p 80:80 auth`<br>
Access: `http://localhost:80/docs`


## Development
Build: `docker build -f Dockerfile.dev -t dev-auth .`<br>
Run: `docker run -p 80:80 dev-auth`<br>
Access: `http://localhost:80/docs`<br>
### or without docker
virtualenv setup: https://www.youtube.com/watch?v=IAvAlS0CuxI<br>
Install requirements: `pip install -r requirements.txt`<br>
Run: `python ./app/main.py`<br>
Access: `http://localhost:8000/docs`<br>



### links 

https://www.youtube.com/watch?v=LaGYxQWYmmc

https://iq.opengenus.org/failed-to-solve-with-frontend-dockerfile-v0/