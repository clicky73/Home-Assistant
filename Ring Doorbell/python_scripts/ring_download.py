# obtain ring doorbell camera object
# replace the camera.front_door by your camera entity
ring_cam = hass.states.get('camera.front_door')
ring_motion = hass.states.get('sensor.front_door_last_activity')
ring_motion2 = 'ring_{}'.format(ring_motion.attributes.get('created_at'))
file_name = ring_motion2[0:18] 

subdir_name = 'ring_{}'.format(ring_cam.attributes.get('friendly_name'))
# get video URL


data = {
    'url': ring_cam.attributes.get('video_url'),
    'subdir': subdir_name,
 #   'filename': ring_motion.attributes.get('created_at')
 #   'filename': ring_motion2 + '.mp4'
 
    'filename': file_name + '.mp4'
}

# call downloader integration to save the video
hass.services.call('downloader', 'download_file', data)