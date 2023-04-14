load("@bazel_gazelle//:def.bzl", "gazelle")
load("@com_github_bazelbuild_buildtools//buildifier:def.bzl", "buildifier")

# gazelle:prefix github.com/sfortson/random-scripts
gazelle(name = "gazelle")

gazelle(
    name = "gazelle-update-repos",
    args = [
        "-to_macro=deps.bzl%go_dependencies",
        "-from_file=go.mod",
        "-prune",
    ],
    command = "update-repos",
)

buildifier(
    name = "buildifier",
)
