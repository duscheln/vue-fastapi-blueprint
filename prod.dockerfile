FROM node:14 as builder 

ADD frontend /usr/app/src/frontend
WORKDIR /usr/app/src/frontend
RUN rm -rf node_modules
RUN npm install 
RUN npm run build 

FROM python:3.8
ADD backend/ /usr/app/src/backend
WORKDIR /usr/app/src/backend
COPY --from=builder /usr/app/src/backend/dist /usr/app/src/backend/dist 
RUN pip install -r pip-requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn" ,"main:app" ,"--host", "0.0.0.0"]
#ENTRYPOINT [ "python" ,"main.py" ]