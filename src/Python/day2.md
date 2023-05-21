# mdBook-specific features

## Hiding code lines

There is a feature in mdBook that lets you hide code lines by prepending them
with a `#` [like you would with Rustdoc][rustdoc-hide].

[rustdoc-hide]: https://doc.rust-lang.org/stable/rustdoc/documentation-tests.html#hiding-portions-of-the-example

```bash
# fn main() {
    let x = 5;
    let y = 6;

    println!("{}", x + y);
# }
```

Will render as

```rust
# fn main() {
    let x = 5;
    let y = 6;

    println!("{}", x + y);
# }