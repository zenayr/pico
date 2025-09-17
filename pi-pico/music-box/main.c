#include "pico/stdlib.h"
#include "pitches.h"
#include "hardware/pwm.h"
#include <stdio.h>

#define buttonPin 14
#define buzzer 15

long map(long x, long in_min, long in_max, long out_min, long out_max){
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

int main(){

    stdio_init_all();
    uint16_t melody[] = {NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4};
    long noteDurations[] = {400, 800, 800, 400, 400, 400, 400,400};

    gpio_init(buttonPin);
    gpio_set_dir(buttonPin, GPIO_IN);

    gpio_set_function(buzzer, GPIO_FUNC_PWM);
    uint slice_num = pwm_gpio_to_slice_num(buzzer);
    uint chanel = pwm_gpio_to_channel(buzzer);
    
    //pwm_set_phase_correct(slice_num, true);
    long pwm_value = map(NOTE_D4, 0, 4095, 0, 255);
    pwm_set_wrap(slice_num, 255);
    pwm_set_chan_level(slice_num, chanel, pwm_value);


     while(true){
        pwm_set_enabled(slice_num, true);    
        sleep_ms(100);
        pwm_set_enabled(slice_num, false);
    }
}