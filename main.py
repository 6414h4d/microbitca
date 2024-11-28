def on_bluetooth_connected():
    music.ring_tone(262)
    music.set_volume(255)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

bluetooth.start_accelerometer_service()