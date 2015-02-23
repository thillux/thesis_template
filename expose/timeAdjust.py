#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
import sys
import datetime

tableHeader = r"""\section*{Zeitplan}
\begin{table}[!ht]
\caption{Zeitplan der Arbeit}
\begin{tabular}{p{0.3\textwidth}p{0.62\textwidth}}

\toprule
\textbf{Datum} & \textbf{Abschnitt}\\
\midrule
"""

tableFooter = r"""\bottomrule
\end{tabular}
\end{table}
"""


def main():
    assert(len(sys.argv) == 3)

    inFile, outFile = sys.argv[1], sys.argv[2]

    dateFormat = "%d.%m.%Y"

    outFile = open(outFile, "w", encoding="utf-8")

    outFile.write(tableHeader)

    with open(inFile, encoding="utf-8") as inData:
        dateJson = json.load(inData)

        startDate = None
        if len(dateJson["referenceDate"]) == 0:
            startDate = datetime.datetime.now()
        else:
            startDate = datetime.datetime.strptime(dateJson["referenceDate"], dateFormat)

        currentDate = startDate
        for item in dateJson["items"]:
            weeks = item["weeks"]
            days = item["days"]

            startPhase = currentDate
            delta = datetime.timedelta(weeks=weeks, days=days - 1)
            endPhase = (currentDate + delta)
            startString = startPhase.strftime(dateFormat)
            endString = endPhase.strftime(dateFormat)

            delta = datetime.timedelta(days=1)

            currentDate = endPhase + delta

            outFile.write("{} -- {} & {} \\\\\n".format(startString, endString, item["title"]))
    outFile.write(tableFooter)

    outFile.close()

if __name__ == "__main__":
    main()
