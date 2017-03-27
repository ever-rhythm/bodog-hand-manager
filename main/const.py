
class Const(object):

    sep = '\n'

    preflop = '*** HOLE CARDS ***'
    flop = '*** FLOP ***'
    turn = '*** TURN ***'
    river = '*** RIVER ***'
    showdown = '*** SHOW DOWN ***'
    summary = '*** SUMMARY ***'

    pairStreet = [ (preflop,preflop) , (flop,flop) , (turn,turn) , (river,river) , (showdown,showdown) ]

    sd = ': Showdown'
    nsd = ': Does not show'
    sbsb = 'small blind'
    bbbb = 'big blind'
    seat = 'Seat '
    me = '[ME]' 
    dealt = 'dealt'
    pot = 'Pot'

    uncall = 'uncalled'
    handresult = 'Hand result'
    deposit = 'deposit'
    posts = 'Posts'

    pairBlind = [ (sbsb,'sb'),(bbbb,'bb') ]

    sb = 'Small'
    bb = 'Big'
    utg = 'UTG'
    md = 'UTG+1'
    co = 'UTG+2'
    btn = 'Dealer'

    pairPos = [ (sb,sb),(bb,bb),(utg,utg),(md,md),(co,co),(btn,btn) ]

    check = 'Checks'
    fold = 'Folds'
    call = 'Calls'
    bet = 'Bets'
    raises = 'Raises'
    allin = 'All-in'

    pairAction = [ (check,check),(fold,fold),(call,call),(bet,bet),(raises,raises),(allin,allin) ]

    hero = 'Hero'
    player = 'Player'
    table = 'Table'
    ps = 'PokerStars'
    nlh = 'Hold\'em No Limit'

