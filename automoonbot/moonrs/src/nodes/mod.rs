mod common;
mod dynamic;
mod statics;
mod tests;

use crate::{data::*, *};
pub use tests::*;
pub use common::*;
pub use nodes::{dynamic::DynamicNode, statics::StaticNode};
use utils::helpers::*;