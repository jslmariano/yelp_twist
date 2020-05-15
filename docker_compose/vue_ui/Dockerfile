FROM node:lts-alpine

# install project dependencies
RUN npm install -g @vue/cli

# set working directory
WORKDIR /vue_ui
RUN ls -al
# # copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
RUN ls -al

# # add `/vue_ui/node_modules/.bin` to $PATH
ENV PATH /vue_ui/node_modules/.bin:$PATH

RUN npm install



# vue ui --headless --port 8000 --host 0.0.0.0
CMD [ "vue", "ui", "--headless" , "--port", "8000",  "--host", "0.0.0.0" ]
