%define device pipa
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Pad 6

%define community_adaptation 1

%define pixel_ratio 1.5

%define android_version_major 14

%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-pipa.inc
%include patterns/patterns-sailfish-device-configuration-pipa.inc
