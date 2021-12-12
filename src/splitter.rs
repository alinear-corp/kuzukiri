use std::collections::{HashMap, HashSet};


pub struct Splitter {
    terminals: HashSet<char>,
    parentheses: HashMap<char, char>,
}

impl Splitter {
    pub fn new(
        terminals: Option<HashSet<char>>,
        parentheses: Option<HashMap<char, char>>
    ) -> Self {
        let terminals = if let Some(ts) = terminals {
            ts
        } else {
            vec! [
                '。', '．', '，', '！', '？', '\n',
            ].into_iter().collect()
        };
        let parens = if let Some(ps) = parentheses {
            ps
        } else {
            vec![
                ('「', '」'),
                ('『', '』'),
                ('（', '）'),
                ('［', '］'),
                ('【', '】'),
            ].into_iter().collect()
        };
        Splitter {
            terminals,
            parentheses: parens,
        }
    }

    pub fn split(&self, text: String) -> Vec<String> {
        let mut sentences: Vec<String> = vec![];
        let mut buf: Vec<char> = vec![];
        let mut waiting_stack: Vec<char> = vec![];

        for c in text.chars() {
            buf.push(c);

            if let Some(t) = self.parentheses.get(&c) {
                waiting_stack.push(t.clone());
            } else if let Some(d) = waiting_stack.last() {
                if c == *d {
                    waiting_stack.pop();
                }
            } else if self.terminals.contains(&c) {
                sentences.push(buf.into_iter().collect());
                buf = vec![];
            }
        }

        if buf.len() > 0 {
            sentences.push(buf.into_iter().collect());
        }

        sentences
    }
}
