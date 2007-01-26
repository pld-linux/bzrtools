Summary:	A collection of utilities and plugins for Bazaar-NG
Summary(pl):	Zbiór narzêdzi i wtyczek dla programu Bazaar-NG
Name:		bzrtools
Version:	0.14.0
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://panoramicfeedback.com/opensource/%{name}-%{version}.tar.gz
# Source0-md5:	5932729e81f19562a6a844be2555a115
URL:		http://bazaar-vcs.org/BzrTools
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python
Requires:	bzr >= 0.14
Requires:	diffutils
Requires:	graphviz >= 2.6
Requires:	librsvg
Requires:	patch
Requires:	rsync >= 2.6.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BzrTools is a collection of plugins for Bazaar-NG (bzr). Among the
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

%description -l pl
BZrTools to zestaw wtyczek do programu Bazaar-NG (bzr). Zestaw zawiera
nastêpuj±ce narzêdzia:
- push - u¿ywa programu rsync do wys³ania lokalnych zmian na zdalny
  serwer
- annotate - wy¶wietla przypisy odno¶nie rewizji w ka¿dej linii pliku
- shelve/unshelve - pozwala na powrót do wcze¶niejszych zmian,
  zatwierdzenia zmian i przywrócenia stanu sprzed dokonania zmian
- clean-tree - usuwa nieznane, ignorowane pliki z projektu
- graph-ancestry - graficzne przedstawienie rodowodu plików w
  projekcie
- shell - interpreter poleceñ bzr z dope³nianiem poleceñ
- patch - pozwala na nak³adanie ³at z pliku lub adresu URL

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS NEWS.Shelf README README.Shelf TODO TODO.Shelf CREDITS
%{py_sitescriptdir}/bzrlib/plugins/bzrtools
