# stringmatch-bench

## Tools

Here provides benchmark tools to compare the performance of the data structures:

### Rust

- [`crawdad::Trie`](https://docs.rs/crawdad/latest/crawdad/trie/struct.Trie.html)
- [`crawdad::MpTrie`](https://docs.rs/crawdad/latest/crawdad/mptrie/struct.MpTrie.html)
- [`yada::DoubleArray`](https://docs.rs/yada/latest/yada/struct.DoubleArray.html)
- [`fst::Map`](https://docs.rs/fst/latest/fst/struct.Map.html)
- [`daachorse::DoubleArrayAhoCorasick`](https://docs.rs/daachorse/latest/daachorse/bytewise/struct.DoubleArrayAhoCorasick.html)
- [`daachorse::CharwiseDoubleArrayAhoCorasick`](https://docs.rs/daachorse/latest/daachorse/charwise/struct.CharwiseDoubleArrayAhoCorasick.html)
- [`std::collections::BTreeMap`](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html)
- [`std::collections::HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [`hashbrown::HashMap`](https://docs.rs/hashbrown/latest/hashbrown/struct.HashMap.html)

You can measure search time and memory usage with your datasets in the following command.

```
$ cargo run --release --bin measure -- -k ../data/unidic/unidic -t ../data/wagahaiwa_nekodearu.txt
```

Or, you can measure search time more accurately with [`criterion.rs`](https://github.com/bheisler/criterion.rs) in the following command.

```
$ cd ./rust
$ cargo bench
```

### Python

- [`ahocorasick_rs`](https://github.com/G-Research/ahocorasick_rs)
- [`daachorse`](https://pypi.org/project/daachorse/)

You can measure search time more accurately with [`pytest`](https://pytest.org/) in the following command.

```
$ cd ./python
$ nox
```

## Disclaimer

This software is developed by LegalForce, Inc.,
but not an officially supported LegalForce product.

## License

Licensed under either of

 * Apache License, Version 2.0
   ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license
   ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

The datasets contained [here](./data) are copied from third party repositories.
Follow the license terms of each software
