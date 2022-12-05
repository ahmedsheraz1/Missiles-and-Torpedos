Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import argparse
parser = argparse.ArgumentParser(prog='HELM')
subparsers = parser.add_subparsers()
parser_l = subparsers.add_parser('launch', help='Launch Control')
parser_l.add_argument('-m', '--missiles', action='store_true')
_StoreTrueAction(option_strings=['-m', '--missiles'], dest='missiles', nargs=0, const=True, default=False, type=None, choices=None, help=None, metavar=None)
parser_l.add_argument('-t', '--torpedos', action='store_true')
_StoreTrueAction(option_strings=['-t', '--torpedos'], dest='torpedos', nargs=0, const=True, default=False, type=None, choices=None, help=None, metavar=None)
parser_m = subparsers.add_parser('move', help='Move Vessel',
                                 aliases=('steer', 'turn'))
parser_m.add_argument('-c', '--course', type=int, required=True)
_StoreAction(option_strings=['-c', '--course'], dest='course', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
parser_m.add_argument('-s', '--speed', type=int, default=0)
_StoreAction(option_strings=['-s', '--speed'], dest='speed', nargs=None, const=None, default=0, type=<class 'int'>, choices=None, help=None, metavar=None)
