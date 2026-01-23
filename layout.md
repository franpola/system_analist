%%kroki d2

spine.spine01: {
  icon: https://svg.infrastructureascode.ch/square/green/sq_switch.svg
}
spine.spine02: {
  shape: image
  icon: https://svg.infrastructureascode.ch/square/green/sq_switch.svg
}

spine.spine01 -- leaf.siteA.leaf01
spine.spine01 -- leaf.siteA.leaf02
spine.spine01 -- leaf.siteB.leaf03
spine.spine02 -- leaf.siteA.leaf01
spine.spine02 -- leaf.siteA.leaf02
spine.spine02 -- leaf.siteB.leaf03