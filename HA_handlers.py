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

#==========LIGHT FUNCTIONS ===================

def scene_api(entity, token):
    ha_url = scene_call
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = entity
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
def light_off_api(entity, token):
    ha_url = light_off_call
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = entity
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
def light_toggle_api(entity, token):
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
    payload = '{"entity_id":"media_player.kitchen_speaker"}'
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()

def volume_down(token):
    ha_url = "http://192.168.0.23:8123/api/services/media_player/volume_down"
    headers = {
      "Authorization": token,
      "content-type": 'application/json',
      }
    payload = '{"entity_id":"media_player.kitchen_speaker"}'
    response = urequests.post(ha_url, headers=headers, data=payload)
    response.close()
    
#=============================================

def key_do(key_number, page_n, token):
    if page_n == 0:
        #Key 5 page 0: cozy studio
        if key_number == 16:
            #print("You pressed button 5")
            scene_api('{"entity_id":"scene.studio_cozy"}', token=token)
        #Key 6 page 0: Warm Bright
        elif key_number == 32:
            #print("You pressed button 6")
            scene_api('{"entity_id":"scene.studio_bright_warm"}', token=token)
        #Key 7 page 0: Cool Bright
        elif key_number == 64:
            #print("You pressed button 7")
            scene_api('{"entity_id":"scene.studio_bright_cool"}', token=token)
        #Key 8 page 0: Studio OFF
        elif key_number == 128:
            #print("You pressed button 7bis")
            scene_api('{"entity_id":"scene.studio_off"}', token=token)
        #Key 8 page 0: Desk Light Red
        elif key_number == 256:
            #print("You pressed button 8")
            scene_api('{"entity_id":"scene.studio_desk_red"}', token=token)
        #Key 9 page 0: Desk Light Warm White
        elif key_number == 512:
            #print("You pressed button 9")
            scene_api('{"entity_id":"scene.studio_desk_warm_white"}', token=token)
        #Key 10 page 0: Desk Light Cool White
        elif key_number == 1024:
            #print("You pressed button 10")
            scene_api('{"entity_id":"scene.studio_desk_cool_white"}', token=token)
        #Key 11 page 0: Desk Light OFF - TO DO
        elif key_number == 2048:
            #print("You pressed button 11")
            light_off_api('{"entity_id":"light.studio_desk_strip"}', token=token)
        #Key 12 page 0: Toggle On Air light
        elif key_number == 4096:
            #print("You pressed button 12")            
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
            #print("You pressed button 13")
            light_toggle_api('{"entity_id":"light.dome_light"}', token=token)
        #Key 14 page 0: Volume UP - TO DO
        elif key_number == 16384:
            #print("You pressed button 14")
            volume_up(token=token)
        #Key 15 page 0: Volume Down - TO DO
        elif key_number == 32768:
            #print("You pressed button 15")
            volume_down(token=token)
            
    if page_n == 1: #Additional lights control for the Studio
        #Key 5 page 0: n5md
        if key_number == 16:
            #print("You pressed button 5")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "https://somafm.com/m3u/n5md130.m3u", "media_content_type": "audio/mp4"}', token=token)
        #Key 6 page 1: SanFran 
        elif key_number == 32:
            #print("You pressed button 6")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "https://somafm.com/m3u/sf1033130.m3u", "media_content_type": "audio/mp4"}', token=token)
        #Key 7 page 1: Drone
        elif key_number == 64:
            #print("You pressed button 7")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "https://somafm.com/m3u/dronezone130.m3u", "media_content_type": "audio/mp4"}', token=token)
        #Key 8 page 1: DarkZone 
        elif key_number == 128:
            #print("You pressed button 7bis")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "https://somafm.com/m3u/darkzone130.m3u", "media_content_type": "audio/mp4"}', token=token)
        #Key 8 page 1: 6forty
        elif key_number == 256:
            #print("You pressed button 8")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "http://radio.6forty.com:8000/6forty.m3u", "media_content_type": "audio/mp4"}', token=token)
        #Key 9 page 1: BBC 3
        elif key_number == 512:
            print("You pressed button 9")
        #Key 10 page 1: BBC 4
        elif key_number == 1024:
            print("You pressed button 10")
        #Key 11 page 1: KEXP
        elif key_number == 2048:
            #print("You pressed button 11")
            start_radio('{"entity_id":"media_player.kitchen_speaker", "media_content_id": "https://kexp.streamguys1.com/kexp160.aac", "media_content_type": "audio/mp4"}', token=token)
        #Key 12 page 1: TBC
        elif key_number == 4096:
            print("You pressed button 12")            
        #Key 13 page 1: Stop Radio
        elif key_number == 8192:
            #print("You pressed button 13")
            ha_url = radio_stop
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"media_player.kitchen_speaker"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 14 page 0: Volume UP - TO DO
        elif key_number == 16384:
            #print("You pressed button 14")
            volume_up(token=token)
        #Key 15 page 0: Volume Down - TO DO
        elif key_number == 32768:
            #print("You pressed button 15")
            volume_down(token=token)
    if page_n == 2: #Possibly move the radio controls to this page
        print("see you later")
    if page_n == 3: #Controls for lights and automations around the house
        print("see you later")
        
    return
