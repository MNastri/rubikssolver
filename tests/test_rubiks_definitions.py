from rubikssolver.rubiks_definitions import get_edge_name_from


class TestGetEdgeNameFrom:
    def test_ur(self):
        edge_number = 0
        assert get_edge_name_from(edge_number) == "UR"

    def test_uf(self):
        edge_number = 1
        assert get_edge_name_from(edge_number) == "UF"

    def test_ul(self):
        edge_number = 2
        assert get_edge_name_from(edge_number) == "UL"

    def test_ub(self):
        edge_number = 3
        assert get_edge_name_from(edge_number) == "UB"

    def test_dr(self):
        edge_number = 4
        assert get_edge_name_from(edge_number) == "DR"

    def test_df(self):
        edge_number = 5
        assert get_edge_name_from(edge_number) == "DF"

    def test_dl(self):
        edge_number = 6
        assert get_edge_name_from(edge_number) == "DL"

    def test_db(self):
        edge_number = 7
        assert get_edge_name_from(edge_number) == "DB"

    def test_fr(self):
        edge_number = 8
        assert get_edge_name_from(edge_number) == "FR"

    def test_fl(self):
        edge_number = 9
        assert get_edge_name_from(edge_number) == "FL"

    def test_bl(self):
        edge_number = 10
        assert get_edge_name_from(edge_number) == "BL"

    def test_br(self):
        edge_number = 11
        assert get_edge_name_from(edge_number) == "BR"
