from television import Television

def main():
    tv = Television()

    print(tv)
    tv.power()
    print(tv)

    tv.channel_up()
    tv.channel_up()
    print(tv)

    tv.volume_up()
    tv.volume_up()
    print(tv)

    tv.mute()
    print(tv)

    tv.mute()
    print(tv)

if __name__ == "__main__":
    main()
