def get_quotes (lang='all', level='primary'):
    if lang == 'all':
        return set('«»"\'<>‹›„“‚‘’⹂”「」『』﹃﹄﹁﹂《》〈〉⟪⟫⟨⟩❝❞❛❜〝〞〟❮❯')
        
    if level == 'primary':
        match lang:
            case 'af' | 'nl':
                return [('“', '”'), ('„', '”')]
            case 'ar':
                return [('«', '»'), ('”', '“')]
            case 'hy' | 'el' | 'fa' | 'io' | 'kk' | 'km' | 'ps' | 'rm' | 'ug':
                return [('«', '»')]
            case 'am' | 'ca' | 'es' | 'eu' | 'gl' | 'it' | 'oc' | 'ru' | 'ti':
                return [('«', '»'), ('“', '”')]
            case 'az' | 'be' | 'no' | 'uz':
                return [('«', '»'), ('„', '“')]
            case 'bg' | 'et':
                return [('„', '“'), ('«', '»')]
            case 'bs':
                return [('”', '”'), ('„', '”'), ('„', '“')]
            case 'cs' | 'sk' | 'sl':
                return [('„', '“'), ('»', '«')]
            case 'da':
                return [('»', '«'), ('“', '”'), ('”', '”'), ('„', '“')]
            case 'de':
                return [('„', '“'), ('»', '«'), ('«', '»')]
            case 'en':
                return [('“', '”'), ('‘', '’')]
            case 'eo':
                return [('“', '”'), ('«', '»'), ('„', '“')]
            case 'fi':
                return [('”', '”'), ('»', '»')]
            case 'fil' | 'ga' | 'hi' | 'ia' | 'lo' | 'mt' | 'ta' | 'th' | 'ur' | 'vi':
                return [('“', '”')]
            case 'fr':
                return [('« ', ' »'), ('“', '”'), ('«', '»')]
            case 'cy' | 'gd':
                return [('‘', '’'), ('“', '”')]
            case 'he':
                return [('"', '"'), ('”', '„')]
            case 'hr':
                return [('„', '”'), ('»', '«')]
            case 'hu' | 'ro':
                return [('„', '”')]
            case 'id':
                return [('“', '”'), ('”', '”')]
            case 'is' | 'ka' | 'lt' | 'mk' | 'sq' | 'wen':
                return [('„', '“')]
            case 'ja':
                return [('「', '」'), ('﹁', '﹂')]
            case 'jbo':
                return [('lu ', ' li’u')]
            case 'kl':
                return [('"', '"'), ('»', '«')]
            case 'ko':
                return [('“', '”'), ('﹃', '﹄'), ('《', '》')]
            case 'bo' | 'khb' | 'tdd':
                return [('《', '》')]
            case 'lv':
                return [('“', '”'), ('„', '“')]
            case 'mn':
                return [('«', '»'), ('„', '“'), ('⟪', '⟫')]
            case 'pl':
                return [('„', '”'), ('«', '»')]
            case 'pt' | 'tr':
                return [('“', '”'), ('«', '»')]
            case 'sr':
                return [('„', '”'), ('„', '“'), ('»', '«')]
            case 'sv':
                return [('”', '”'), ('»', '»'), ('«', '«')]
            case 'uk':
                return [('«', '»'), ('„', '“'), ('„', '”')]
            case 'zh':
                return [('「', '」'), ('﹁', '﹂'), ('“', '”'), ('﹃', '﹄')]
            case _:
                return []
            
    if level == 'secondary':
        match lang:
            case 'af' | 'nl':
                return [('‘', '’'), ('‚', '’')]
            case 'am' | 'ti':
                return [('‹', '›'), ('‘', '’')]
            case 'az' | 'be':
                return [('„', '“')]
            case 'bs':
                return [('’', '’'), ('»', '«')]
            case 'bg':
                return [('’', '’'), ('‘', '’')]
            case 'ca' | 'cy' | 'es' | 'eu' | 'gl' | 'gd' | 'uk':
                return [('“', '”'), ('‘', '’')]
            case 'cs' | 'sk' | 'sl':
                return [('‚', '‘'), ('›', '‹')]
            case 'da':
                return [('›', '‹'), ('‘', '’'), ('’', '’')]
            case 'de':
                return [('‚', '‘'), ('›', '‹'), ('“', '”')]
            case 'el' | 'kk' | 'km':
                return [('“', '”')]
            case 'en' | 'pt':
                return [('‘', '’'), ('“', '”')]
            case 'eo':
                return [('‘', '’'), ('‹', '›'), ('‚', '‘')]
            case 'fi' | 'sr':
                return [('’', '’')]
            case 'fil' | 'ga' | 'hi' | 'hr' | 'ia' | 'ta' | 'th' | 'ur':
                return [('‘', '’')]
            case 'fr':
                return [('« ', ' »'), ('“', '”'), ('‹ ', ' ›'), ('‘', '’')]
            case 'he':
                return [('\'', '\''), ('’', ',')]
            case 'hu':
                return [('»', '«')]
            case 'id':
                return [('‘', '’'), ('’', '’')]
            case 'is' | 'lt' | 'wen':
                return [('‚', '‘')]
            case 'it':
                return [('“', '”'), ('‘', '’'), ('‹ ', ' ›')]
            case 'io' | 'mt'| 'sq':
                return [('‘', '’')]
            case 'ja':
                return [('『', '』'), ('﹃', '﹄')]
            case 'jbo':
                return [('lu “', '” li’u')]
            case 'bo' | 'khb' | 'tdd':
                return [('〈', '〉')]
            case 'ko':
                return [('‘', '’'), ('﹁', '﹂'), ('〈', '〉')]
            case 'mk':
                return [('’', '‘')]
            case 'mn':
                return [('„', '“'), ('⟨', '⟩')]
            case 'no':
                return [('‘', '’'), (',', '‘')]
            case 'oc':
                return [('“', '”'), ('«', '»')]
            case 'pl':
                return [('»', '«'), ('‘', '’')]
            case 'rm' | 'ug':
                return [('‹', '›')]
            case 'ro' | 'vi':
                return [('«', '»')]
            case 'ru':
                return [('„', '“'), ('‘', '’')]
            case 'sv':
                return [('’', '’')]
            case 'tr':
                return [('‘', '’'), ('‹', '›')]
            case 'uz':
                return [('„', '“'), ('‚', '‘')]
            case 'zh':
                return [('『', '』'), ('﹃', '﹄'), ('‘', '’'), ('﹁', '﹂')]
            case _:
                return []
            
def quotes_to_str_by_lang (lang):
    quotes_list = []
    for q in get_quotes(lang):
        for c in q:
            quotes_list.append(c)
    return ''.join(sorted(quotes_list))

def brackets_to_str (brackets):
    brackets_list = []
    for b in brackets:
        for c in b:
            brackets_list.append(c)
    return ''.join(sorted(brackets_list))