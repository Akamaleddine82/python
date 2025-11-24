from television import Television

def main():
    tv = Television()

    print("Initial:", tv)

    # Power on
    tv.power()
    print("After power on:", tv)

    # Channel up a few times
    tv.channel_up()
    print("Channel up 1:", tv)

    tv.channel_up()
    print("Channel up 2:", tv)

    # Channel down
    tv.channel_down()
    print("Channel down:", tv)

    # Volume up
    tv.volume_up()
    print("Volume up:", tv)

    # Volume down
    tv.volume_down()
    print("Volume down:", tv)

    # Mute
    tv.mute()
    print("Muted:", tv)

    # Unmute
    tv.mute()
    print("Unmuted:", tv)

    # Power off
    tv.power()
    print("After power off:", tv)


if __name__ == "__main__":
    main()
