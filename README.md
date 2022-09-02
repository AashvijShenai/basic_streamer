# basic_streamer
Simple script to stream camera feed to a web server using flask

Required modules:
1. flask (pip install flask)
2. opencv (pip install opencv-python)

Run:
1. Enter "python streamer.py" on terminal
2. Wait till you receive the message "Running on http://0.0.0.0:<port>/ (Press CTRL+C to quit)"
3. Open browser and navigate to http://<IP>:<port> or if you are local- localhost:<port>
   where <IP> is the IP of the machine
         <port> is the server port (default - 2204)
4. Quit by using Ctrl+C
