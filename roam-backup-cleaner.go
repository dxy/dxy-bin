/*
Program roam-backup-cleaner deletes old backup files generated by Roam.

Old backups are stored in Backblaze so simply removing older ones should be
fine.
*/
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"time"
)

func Usage() {
	fmt.Printf("Usage: %s --dir=backup_directory\n", os.Args[0])
	flag.PrintDefaults()
}

func CleanUpFiles(d string, exp time.Duration, dry_run bool) {
	now := time.Now()
	files, err := ioutil.ReadDir(d)
	if err != nil {
		log.Fatal(err)
	}
	for _, f := range files {
		age := now.Sub(f.ModTime())
		if age < exp {
			continue
		}
		fmt.Printf("%s eligible for deletion\n", f.Name())
		if dry_run {
			continue
		}
		os.Remove(filepath.Join(d, f.Name()))
		// TODO: If older than N days (e.g. 3), keeping one daily (vs hourly) backup will suffice.
	}
}

func main() {
	dir := flag.String("dir", "", "the name of the directory where Roam backup files are stored")
	exp := flag.Duration("expiration", 120*time.Hour, "age of a backup at which it gets deleted")
	dry_run := flag.Bool("dry_run", false, "whether files get deleted")
	flag.Usage = Usage
	flag.Parse()

	if *dir == "" {
		Usage()
		os.Exit(1)
	}
	if _, err := os.Stat(*dir); os.IsNotExist(err) {
		log.Fatal(err)
	}
	CleanUpFiles(*dir, *exp, *dry_run)
}
