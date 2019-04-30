open IN, '<' , 'hitmix.fasta.clstr';
my @tmp_list;
my %list;
my $add_flag=1;

my $line=<IN>;

while($line=<IN>) {
	if ($line=~/^>/) {
		if ($add_flag==1) {	
			foreach my $id (@tmp_list) {
				$list{$id}=1;
			}
		}
		$add_flag=1;
		@tmp_list=();
	} elsif ($line=~/(>\d+_pat_)\.\.\./) {
		push(@tmp_list,$1);
	} elsif ($line=~/(>\d+#vi#)\.\.\./) {
		$add_flag=0;
	}
}

if ($add_flag==1) {
	foreach my $id (@tmp_list) {
		$list{$id}=1;
	}
}


open INDEX ,'<', "indexed_all_phage_orf_pat.index";

my %index_hash;
while(<INDEX>) {
	chomp;
	my @f=split(/\t/,$_);
	$index_hash{$f[0]}=$f[1];
}


open FASTA , '<' , 'indexed_all_phage_orf_pat.fasta';
my $print_flag=0;

while(<FASTA>) {
	chomp;
	if (/^>/) {
		$print_flag=0;
		if ($list{$_}) {	
			$print_flag=1;
			$_=$index_hash{$_};
		}
	}
	print "$_\n" if ($print_flag==1);
}
	

