mkdir -p ~/.streamlit/

echo "\
[general]\n\
email=\"dev182000@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = trye\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml