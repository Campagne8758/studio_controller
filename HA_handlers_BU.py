#Handles button presses and calls to Home assistant
import urequests

scene_call = "http://192.168.0.23:8123/api/services/scene/turn_on"
light_toggle_call = "http://192.168.0.23:8123/api/services/light/toggle"
switch_toggle_call = "http://192.168.0.23:8123/api/services/switch/toggle"
light_off_call = "http://192.168.0.23:8123/api/services/light/turn_off"

def key_do(key_number, page_n, token):
    if page_n == 0:
        #Key 5 page 0: cozy studio
        if key_number == 16:
            #print("You pressed button 5")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_cozy"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 6 page 0: Warm Bright
        elif key_number == 32:
            #print("You pressed button 6")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_bright_warm"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 7 page 0: Cool Bright
        elif key_number == 64:
            #print("You pressed button 7")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_bright_cool"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 8 page 0: Studio OFF
        elif key_number == 128:
            #print("You pressed button 7bis")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_off"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 8 page 0: Desk Light Red
        elif key_number == 256:
            #print("You pressed button 8")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_desk_red"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 9 page 0: Desk Light Warm White
        elif key_number == 512:
            #print("You pressed button 9")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_desk_warm_white"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 10 page 0: Desk Light Cool White
        elif key_number == 1024:
            #print("You pressed button 10")
            ha_url = scene_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"scene.studio_desk_cool_white"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 11 page 0: Desk Light OFF - TO DO
        elif key_number == 2048:
            #print("You pressed button 11")
            ha_url = light_off_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"light.studio_desk_strip"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
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
            ha_url = light_toggle_call
            headers = {
              "Authorization": token,
              "content-type": 'application/json',
              }
            payload = '{"entity_id":"light.dome_light"}'
            response = urequests.post(ha_url, headers=headers, data=payload)
            response.close()
        #Key 14 page 0: Volume UP - TO DO
        elif key_number == 16384:
            print("You pressed button 14")
        #Key 15 page 0: Volume Down - TO DO
        elif key_number == 32768:
            print("You pressed button 15")
            
    if page_n == 1:
        print("see you later")
    if page_n == 2:
        print("see you later")
    if page_n == 3:
        print("see you later")
        
    return