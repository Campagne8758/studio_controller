#Handles button presses and calls to Home assistant
import urequests


#Light URLs
scene_call = "http://192.168.0.23:8123/api/services/scene/turn_on"
light_toggle_call = "http://192.168.0.23:8123/api/services/light/toggle"
switch_toggle_call = "http://192.168.0.23:8123/api/services/switch/toggle"
light_off_call = "http://192.168.0.23:8123/api/services/light/turn_off"
#Radio URLs
radio_start = "http://192.168.0.23:8123/api/services/media_player/play_media"
radio_stop = "http://192.168.0.23:8123/api/services/media_player/media_stop"
#Other URLs
script_url = "http://192.168.0.23:8123/api/services/script/turn_on"

# media player global variable to make it easier to migrate to different speaker
MEDIA_PLAYER = 'media_player.studio'

def temp():
    '''placeholder function to be removed after development is terminated'''
    print("placeholder")

#==========LIGHT FUNCTIONS ===================

def scene_api(entity, token):
    '''Takes scene entity name '{"entity_id":"scene.studio_cozy"}' and the token=token variable to recall an Home Assistant scene'''
    ha_url = scene_call
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = entity
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
def light_off_api(entity, token):
    '''Takes light entity name '{"entity_id":"light.example"}' and the token=token variable to turn off a light'''
    ha_url = light_off_call
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = entity
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
def light_toggle_api(entity, token):
    '''Takes light entity name '{"entity_id":"scene.studio_cozy"}' and the token=token variable to toggle the state of a light (ON/OFF)'''
    ha_url = light_toggle_call
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = entity
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()

#=============================================

#==========RADIO FUNCTIONS ===================
#Function to start a radio based on the data payload passed to it by the call
def start_radio(data, token):
    ha_url = radio_start
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = data
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
def volume_up(token):
    ha_url = "http://192.168.0.23:8123/api/services/media_player/volume_up"
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = f'{{"entity_id":"{MEDIA_PLAYER}"}}'
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()

def volume_down(token):
    ha_url = "http://192.168.0.23:8123/api/services/media_player/volume_down"
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = f'{{"entity_id":"{MEDIA_PLAYER}"}}'
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
#=============================================

#============OTHER FUNCTIONS=================

def start_script(data, token):
    '''Start a script, data requires a string in the format: '{"entity_id":"script.cloudy_day_kitchen_automation_on"}' '''
    ha_url = script_url
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = data
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()


def key_do(key_number, page_n, token):
    if page_n == 0:
        #Key 5 page 0: cozy studio
        if key_number == 16:
            scene_api('{"entity_id":"scene.studio_cozy"}', token=token)
        #Key 6 page 0: Warm Bright
        elif key_number == 32:
            scene_api('{"entity_id":"scene.studio_bright_warm"}', token=token)
        #Key 7 page 0: Cool Bright
        elif key_number == 64:
            scene_api('{"entity_id":"scene.studio_bright_cool"}', token=token)
        #Key 8 page 0: Studio OFF
        elif key_number == 128:
            scene_api('{"entity_id":"scene.studio_off"}', token=token)
        #Key 8 page 0: Desk Light Red
        elif key_number == 256:
            scene_api('{"entity_id":"scene.studio_desk_red"}', token=token)
        #Key 9 page 0: Desk Light Warm White
        elif key_number == 512:
            scene_api('{"entity_id":"scene.studio_desk_warm_white"}', token=token)
        #Key 10 page 0: Desk Light Cool White
        elif key_number == 1024:
            scene_api('{"entity_id":"scene.studio_desk_cool_white"}', token=token)
        #Key 11 page 0: Desk Light OFF - TO DO
        elif key_number == 2048:
            light_off_api('{"entity_id":"light.studio_desk_strip"}', token=token)
        #Key 12 page 0: Toggle On Air light
        elif key_number == 4096:         
            ha_url = switch_toggle_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"switch.onair"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 13 page 0:	TOGGLE Dome
        elif key_number == 8192:
            light_toggle_api('{"entity_id":"light.dome_light"}', token=token)
        #Key 14 page 0: Volume UP - TO DO
        elif key_number == 16384:
            volume_up(token=token)
        #Key 15 page 0: Volume Down - TO DO
        elif key_number == 32768:
            volume_down(token=token)
            

            
    if page_n == 1: #Additional lights control for the Studio
        #Key 5 page 1: Shelves warm
        if key_number == 16:
            scene_api('{"entity_id":"scene.studio_shelves_warm"}', token=token)
        #Key 6 page 1: Shelves Red
        elif key_number == 32:
            scene_api('{"entity_id":"scene.studio_shelves_red"}', token=token)
            #Key 7 page 1: Shelves Cool 
        elif key_number == 64:
            scene_api('{"entity_id":"scene.studio_shelves_cool"}', token=token)
        #Key 8 page 1: Shelves OFF 
        elif key_number == 128:
            light_off_api('{"entity_id":"light.studio_shelves"}', token=token)
            #Key 8 page 1: Big light studio warm on
        elif key_number == 256:
            scene_api('{"entity_id":"scene.main_studio_warm"}', token=token)
        #Key 9 page 1: Big Light studio warm dim
        elif key_number == 512:
            scene_api('{"entity_id":"scene.main_studio_warm_dim"}', token=token)
        #Key 10 page 1: Big Light Studio Cool
        elif key_number == 1024:
            scene_api('{"entity_id":"scene.main_studio_cool"}', token=token)
        #Key 11 page 1: Big Light studio off
        elif key_number == 2048:
            light_toggle_api('{"entity_id":"light.studio_main"}', token=token)
        #Key 12 page 1: Studio all off
        elif key_number == 4096:
            scene_api('{"entity_id":"scene.studio_off"}', token=token)
        #Key 13 page 1: Stop Radio
        elif key_number == 8192:
            ha_url = radio_stop
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = f'{{"entity_id":"{MEDIA_PLAYER}"}}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 14 page 0: Volume UP - TO DO
        elif key_number == 16384:
            volume_up(token=token)
        #Key 15 page 0: Volume Down - TO DO
        elif key_number == 32768:
            volume_down(token=token)
           
    if page_n == 2: #Radio controls
        #Key 5 page 0: n5md
        if key_number == 16:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "aac://https://ice2.somafm.com/n5md-128-aac", "media_content_type": "music"}}', token=token)
        #Key 6 page 1: SanFran 
        elif key_number == 32:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "aac://http://ice4.somafm.com/sf1033-128-aac", "media_content_type": "music"}}', token=token)
        #Key 7 page 1: Drone
        elif key_number == 64:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "aac://http://ice2.somafm.com/dronezone-128-aac", "media_content_type": "music"}}', token=token)
        #Key 8 page 1: DarkZone 
        elif key_number == 128:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "aac://http://ice1.somafm.com/darkzone-128-aac", "media_content_type": "music"}}', token=token)
        #Key 8 page 1: 6forty
        elif key_number == 256:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "x-rincon-mp3radio://http://radio.6forty.com:8000/6forty", "media_content_type": "music"}}', token=token)
        #Key 9 page 1: BBC 3
        elif key_number == 512:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "hls-radio://http://lstn.lv/bbc.m3u8?station=bbc_radio_three&bitrate=320000", "media_content_type": "music"}}', token=token)
        #Key 10 page 1: BBC Radio 4
        elif key_number == 1024:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "hls-radio://http://lstn.lv/bbc.m3u8?station=bbc_radio_fourfm&bitrate=320000", "media_content_type": "music"}}', token=token)
        #Key 11 page 1: KEXP
        elif key_number == 2048:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "aac://https://kexp.streamguys1.com/kexp160.aac", "media_content_type": "music"}}', token=token)
        #Key 12 page 1: BBC radio6 Music
        elif key_number == 4096:
            start_radio(f'{{"entity_id":"{MEDIA_PLAYER}", "media_content_id": "hls-radio://http://lstn.lv/bbc.m3u8?station=bbc_6music&bitrate=320000", "media_content_type": "music"}}', token=token)
        #Key 13 page 1: Stop Radio
        elif key_number == 8192:
            ha_url = radio_stop
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = f'{{"entity_id":"{MEDIA_PLAYER}"}}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 14 page 0: Volume UP
        elif key_number == 16384:
            volume_up(token=token)
        #Key 15 page 0: Volume Down
        elif key_number == 32768:
            volume_down(token=token)
            
    if page_n == 3: # Additional controls for lights and automations around the house
        #Key 5 page 0: Bedroom Bright
        if key_number == 16:
            scene_api('{"entity_id":"scene.bedroom_100"}', token=token)
        #Key 6 page 1: Bedroom OFF
        elif key_number == 32:
            scene_api('{"entity_id":"scene.bedroom_off"}', token=token)
        #Key 7 page 1: Lights ON scene
        elif key_number == 64:
            scene_api('{"entity_id":"scene.lights_on"}', token=token)
        #Key 8 page 1: Living room OFF
        elif key_number == 128:
            light_off_api('{"entity_id":"light.living_room_group"}', token=token)
        #Key 8 page 1: TBC
        elif key_number == 256:
            temp()
        #Key 9 page 1: TBC
        elif key_number == 512:
            temp()
        #Key 10 page 1: TBC
        elif key_number == 1024:
            temp()
        #Key 11 page 1: Kitchen movement automation toggle between cloudy and sunny day
        elif key_number == 2048:
            start_script('{"entity_id":"script.kitchen_automation_toggle"}', token = token)
        #Key 12 page 1: Studio OFF
        elif key_number == 4096:
            scene_api('{"entity_id":"scene.studio_off"}', token=token)
        #Key 13 page 1: Stop Radio
        elif key_number == 8192:
            ha_url = radio_stop
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = f'{{"entity_id":"{MEDIA_PLAYER}"}}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 14 page 0: Volume UP
        elif key_number == 16384:
            volume_up(token=token)
        #Key 15 page 0: Volume Down
        elif key_number == 32768:
            volume_down(token=token)
        
    return
