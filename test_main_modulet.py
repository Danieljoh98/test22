from main_module import isLeapYear
import pytest

#fikk komentar: Husk når oppgaven ber deg lage en metode som heter isLeapYear(), så skal den hete det - og ikke noe annet. men i pytest må man starte tester med test_ . samme som i videoen til Mats. viss ikke det var snakk om i main module filen 

# old test
@pytest.mark.parametrize("year", [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 400, 800, 1200, 1600, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 2000 , 2020])
def test_isLeapYear(year):
    assert isLeapYear(year) == True
    assert not isLeapYear(year) == False

# new test Når det er delelig med 4, men ikke 100
@pytest.mark.parametrize("year", [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 404, 804, 1204, 1604, 1608, 1612, 1616, 1620, 1624, 1628, 1632, 1636, 1640, 1644, 1648, 1652, 1656, 1660, 1664, 1668, 1672, 1676, 1680, 1684, 1688, 1692, 1696, 1704, 1708, 1712, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 2020])
def test_isLeapYearDevidedByFourButNotOneHundred(year):
    assert year % 4 == 0 and year % 100 != 0

# new test Når det er delelig med 400
@pytest.mark.parametrize("year", [400, 1200, 800, 1600, 2000 ,2400, 2800, 3200, 3600, 4000])
def test_isLeapYearDevidedByFouHundred(year):
    assert year % 400 == 0



# gammel Et år er ikke et skuddår
@pytest.mark.parametrize("year", [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 59, 61, 62, 63, 65, 66, 67, 69, 70, 71, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89, 90, 91, 93, 94, 95, 97, 98, 99, 100, 200, 300, 500, 600, 700, 900, 1000, 1100, 1201, 1300, 1500, 1700, 1800, 1900, 2100])
def test_isNotLeapYear(year):
    assert isLeapYear(year) == False
    assert not isLeapYear(year) == True

# new test Når det ikke er delelig med 4
@pytest.mark.parametrize("year", [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 59, 61, 62, 63, 65, 66, 67, 69, 70, 71, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89, 90, 91, 93, 94, 95, 97, 98, 99, 501, 601, 701, 901, 1001, 1101, 1201, 1301, 1501, 1701, 1801, 1901])
def test_isNotLeapYearWhenDevidedByFour(year):
    assert  year % 4 != 0

# new test Når det er delelig med 100, men ikke 400.
@pytest.mark.parametrize("year", [100, 200, 300, 500, 600, 700, 900, 1000, 1100, 1300, 1500, 1700, 1800, 1900, 2100, 2200, 2300])
def test_isNotLeapYearWhenDevidedByOneHundredButNotFourHundred(year):
    assert year % 100 == 0 and year % 400 != 0





