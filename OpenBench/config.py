# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#   OpenBench is a chess engine testing framework authored by Andrew Grant.   #
#   <https://github.com/AndyGrant/OpenBench>           <andrew@grantnet.us>   #
#                                                                             #
#   OpenBench is free software: you can redistribute it and/or modify         #
#   it under the terms of the GNU General Public License as published by      #
#   the Free Software Foundation, either version 3 of the License, or         #
#   (at your option) any later version.                                       #
#                                                                             #
#   OpenBench is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU General Public License for more details.                              #
#                                                                             #
#   You should have received a copy of the GNU General Public License         #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

USE_CROSS_APPROVAL = False

OPENBENCH_CONFIG = {

    # Server Client version control
    'client_version' : '4',

    # Generic Error Messages useful to those setting up their own instance
    'error' : {
        'disabled' : 'Account has not been enabled. Contact me@shaheryarsohail.com',
        'fakeuser' : 'This is not a real Finding Chess User. Create a proper Finding Chess account.',
    },

    # Link to the repo on the sidebar, as well as the core files
    'framework' : 'https://github.com/TheBlackPlague/FindingChess',
    'corefiles' : 'https://raw.githubusercontent.com/TheBlackPlague/FindingChess/master/CoreFiles',

    # Test Configuration. For both SPRT and Fixed Games Tests

    'tests' : {
        'max_games'  : '20000',        # Default for Fixed Games
        'confidence' : '[0.05, 0.05]', # SPRT Type I/II Confidence
    },

    # Book Configuration. When addding a book, follow the provided template.
    # The SHA is defined by hashlib.sha256(book.read().encode('utf-8')).hexdigest().
    # Client.py has this exact code to generate and verify sha256 values, as an example.

    'books' : {
        'UHO_XXL_+0.90_+1.19.epd' : {
            'name'    : 'UHO_XXL_+0.90_+1.19.epd',
            'sha'     : 'a5730bf6c0f68c4abda214c2ae6686c8f0e3dc7426bd17546d958e7063e9ae7e',
            'source'  : 'https://raw.githubusercontent.com/TheBlackPlague/FindingChess/master/Books/UHO_XXL_+0.90_+1.19.epd.zip',
        },
    },


    # Engine Configuration. All engines must have a name, a source repo,
    # a set of paramaters for each standard test type, as well as a scaled
    # NPS value, which is used to normalize speed across all workers.

    'engines' : {

        'StockDory' : {
            'nps': 3200000,
            'base': 'master',
            'book': 'UHO_XXL_+0.90_+1.19.epd',
            'bounds': '[0.00, 5.00]',
            'source': 'https://github.com/TheBlackPlague/StockDory',

            'build' : {
                'path': '',
                'compilers': ['clang>=16.0.0'],
                'cpuflags': ['POPCNT']
            },

            'testmodes' : [
                { 'id' : 'STC',                'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1' },
                { 'id' : 'LTC',                'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6' },
                { 'id' : 'SMP STC',            'th' : 4, 'hash' :   64, 'tc' : '10.0+0.1' },
                { 'id' : 'SMP LTC',            'th' : 4, 'hash' : 1024, 'tc' : '60.0+0.6' },
                { 'id' : 'STC Simplification', 'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'LTC Simplification', 'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'STC Progression',    'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'games' : 20000 },
                { 'id' : 'LTC Progression',    'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'games' : 20000 },
            ]
        },

        'WhiteCore' : {
            'nps': 2200000,
            'base': 'master',
            'book': 'UHO_XXL_+0.90_+1.19.epd',
            'bounds': '[0.00, 5.00]',
            'source': 'https://github.com/SzilBalazs/WhiteCore',

            'build' : {
                'path': '',
                'compilers': ['clang>=16.0.0'],
                'cpuflags': ['POPCNT']
            },

            'testmodes' : [
                { 'id' : 'STC',                'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1' },
                { 'id' : 'LTC',                'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6' },
                { 'id' : 'SMP STC',            'th' : 4, 'hash' :   64, 'tc' : '10.0+0.1' },
                { 'id' : 'SMP LTC',            'th' : 4, 'hash' : 1024, 'tc' : '60.0+0.6' },
                { 'id' : 'STC Simplification', 'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'LTC Simplification', 'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'STC Progression',    'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'games' : 20000 },
                { 'id' : 'LTC Progression',    'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'games' : 20000 },
            ]
        },

        'Mess' : {

            'nps'    : 800000,
            'base'   : 'master',
            'book'   : 'UHO_XXL_+0.90_+1.19.epd',
            'bounds' : '[0.00, 5.00]',
            'source' : 'https://laptudirm.com/x/mess',

            'build' : {
                'path'      : '',
                'compilers' : ['go>=1.20.0'],
                'cpuflags'  : [],
            },

            'testmodes' : [
                { 'id' : 'STC',                'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1' },
                { 'id' : 'LTC',                'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6' },
                { 'id' : 'SMP STC',            'th' : 4, 'hash' :   64, 'tc' : '10.0+0.1' },
                { 'id' : 'SMP LTC',            'th' : 4, 'hash' : 1024, 'tc' : '60.0+0.6' },
                { 'id' : 'STC Simplification', 'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'LTC Simplification', 'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'bounds' : '[-3.00, 1.00]' },
                { 'id' : 'STC Progression',    'th' : 1, 'hash' :   16, 'tc' : '10.0+0.1', 'games' : 20000 },
                { 'id' : 'LTC Progression',    'th' : 1, 'hash' :  256, 'tc' : '60.0+0.6', 'games' : 20000 },
            ],
        },

    },
}
