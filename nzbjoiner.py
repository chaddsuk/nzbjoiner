#!/usr/bin/python3

import argparse
import xml.etree.ElementTree as ET

def merge_nzb_files(nzb_file1, nzb_file2, output_file):
    # Parse the first NZB file
    tree1 = ET.parse(nzb_file1)
    root1 = tree1.getroot()

    # Parse the second NZB file
    tree2 = ET.parse(nzb_file2)
    root2 = tree2.getroot()

    # Find the 'file' elements in both NZB files
    files1 = root1.findall('file')
    files2 = root2.findall('file')

    # Append the files from the second NZB to the first
    for file in files2:
        root1.append(file)

    # Write the merged content to a new NZB file
    tree1.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge two NZB files into one.')
    parser.add_argument('nzb_file1', help='Path to the first NZB file')
    parser.add_argument('nzb_file2', help='Path to the second NZB file')
    parser.add_argument('output_file', help='Output file to save the merged content')

    args = parser.parse_args()
    merge_nzb_files(args.nzb_file1, args.nzb_file2, args.output_file)
