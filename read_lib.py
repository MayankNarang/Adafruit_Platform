import Adafruit_IO as AIO
io=AIO.Client("Mayank_124","aio_zcFu02aQkMz3np84kIhtjZKzFhbT")
while 1:
    print(io.receive("temperature").value)