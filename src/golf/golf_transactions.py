import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    score_dict = {}

    with open(filename, "r", encoding="utf-8") as score_file:
        scores = score_file.readlines()
        for index, score in enumerate(scores):
            name, score = score.split()
            score = int(score)
            score_dict[index] = {"name": name, "score": score}

    reduced_transactions = ReduceTransactions(score_dict)
    print(reduced_transactions.format_response())


class ReduceTransactions(object):
    def __init__(self, scores):
        self.scores = scores
        self.t_dict = {}
        self.build_transaction_dict()
        self.reduce()

    @staticmethod
    def get_owed(debtor, creditor):
        owed = creditor - debtor
        if owed < 0:
            owed = 0
        return owed

    def build_transaction_dict(self):
        name_list = []
        for key, value in self.scores.items():
            name_list.append(key)

        for key, value in self.scores.items():
            d = {}
            for name in name_list:
                d.update({name: self.get_owed(value["score"], self.scores[name]["score"])})
            self.t_dict[key] = d

    def reduce(self):
        n = len(self.t_dict)
        t_dict = self.t_dict

        if n < 2:
            return t_dict

        for i in range(2, n):
            for j in range(0, n - 2):
                first = t_dict[j + 1][0]
                second = t_dict[i][j + 1]

                diff = second - first
                if diff >= 0:
                    t_dict[i][j + 1] = diff
                    t_dict[i][0] = t_dict[i][0] + t_dict[j + 1][0]
                    t_dict[j + 1][0] = 0
                elif diff < 1:
                    t_dict[j + 1][0] = t_dict[j + 1][0] - t_dict[i][j + 1]
                    t_dict[i][0] = t_dict[i][0] + t_dict[i][j + 1]
                    t_dict[i][j + 1] = 0
        return t_dict

    def format_response(self):
        owed_list = []
        for key, value in self.t_dict.items():
            for owed, how_much in value.items():
                if how_much > 0:
                    owed_list.append(
                        f"{self.scores[key]['name']} owes {self.scores[owed]['name']} ${how_much}"
                    )
        return owed_list


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
