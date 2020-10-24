def date_autumn(dates):
    a = reversed(
        sorted(
            sorted(
                sorted(
                    dates,
                    key=lambda x: x.split("-")[1]
                ),
                key=lambda x: x.split("-")[0]
            ),
            key=lambda x: x.split("-")[2]
        )
    )
    for i in a:
        if "09" <= i[0:2] <= "11":
            return i
