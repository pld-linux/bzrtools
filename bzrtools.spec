%define		ver	1.15
%define		minor	0
Summary:	A collection of utilities and plugins for Bazaar
Summary(pl.UTF-8):	Zbiór narzędzi i wtyczek dla programu Bazaar
Name:		bzrtools
Version:	%{ver}.%{minor}
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://code.launchpad.net/bzrtools/stable/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	23f0385123a02e961df63457b4de31e5
URL:		http://bazaar-vcs.org/BzrTools
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	bzr >= %{ver}
Requires:	diffutils
Requires:	graphviz >= 2.6
Requires:	librsvg
Requires:	patch
Requires:	rsync >= 2.6.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BzrTools is a collection of plugins for Bazaar (bzr). Among the
included plugins are:
- push - uses rsync to push local changes to a remote server
- annotate - prints a file annotated with the revision next to each
  line
- shelve/unshelve - allows you to undo some changes, commit, and
  restore
- clean-tree - remove unknown, ignored-junk, or unversioned files from
  the tree
- graph-ancestry - use dot to produce branch ancestry graphs
- shell - a bzr command interpreter with command completion
- patch - apply a patch to your tree from a file or URL

%description -l pl.UTF-8
BZrTools to zestaw wtyczek do programu Bazaar (bzr). Zestaw zawiera
następujące narzędzia:
- push - używa programu rsync do wysłania lokalnych zmian na zdalny
  serwer
- annotate - wyświetla przypisy odnośnie rewizji w każdej linii
  pliku
- shelve/unshelve - pozwala na powrót do wcześniejszych zmian,
  zatwierdzenia zmian i przywrócenia stanu sprzed dokonania zmian
- clean-tree - usuwa nieznane, ignorowane pliki z projektu
- graph-ancestry - graficzne przedstawienie rodowodu plików w
  projekcie
- shell - interpreter poleceń bzr z dopełnianiem poleceń
- patch - pozwala na nakładanie łat z pliku lub adresu URL

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--install-purelib %{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS NEWS.Shelf README README.Shelf TODO TODO.Shelf CREDITS
%{py_sitedir}/bzrlib/plugins/bzrtools
